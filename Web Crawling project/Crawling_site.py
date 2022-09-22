from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
import time
import re

def Change_price(tag):
    display2=Display(visible=0, size=(1920, 1080))
    display2.start()
    driver1= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    URL='https://kream.co.kr/search?keyword='
    # Base_URL=tag#여기에 신발 코드 받기 
    # print(Base_URL)
    driver1.get(URL+f'{tag}')
    try:
        name_click=driver1.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[5]/div/div[3]/div[1]/div/a/div[1]')
        name_click.click()
        time.sleep(2)
        price95=driver1.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/dl/div[4]/dd').text
        filter_pr=re.findall('[0-9]*',price95)
        Final_sp="".join(filter_pr)
    except:
        Final_sp=0
        pass
    return Final_sp



def Search_shoes():
    # chrome_path='chromedriver'
    # driver=webdriver.Chrome(chrome_path)
    display=Display(visible=0, size=(1920, 1080))
    display.start()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.luck-d.com/')
    results=driver.find_element(By.ID,'ogIntro')
    Clicks_group=results.find_elements(By.CSS_SELECTOR,'.agent_site_info img') # 사이트 들어가기agent_site_info
    Information_shoes=[]
    Link_shoes=[]
    Find_shoes=[]

    for Number_click in range(50):
        try:
            #사이트 이름 한국제품인지 확인
            # print('작동확인1')
            results3=driver.find_element(By.ID,'ogIntro')
            korean_filter=results3.find_elements(By.CSS_SELECTOR,'.agent_site_info a')[Number_click].text
            dist_koreaname=re.findall("[가-힣]*[ ]*",korean_filter.rstrip())
            disting_Koreaname2="".join(dist_koreaname)
            
        except:
            pass
        Link_shoes=[]
        
            # 한국에서 파는 제품 아닌거 걸러내기
        if korean_filter in disting_Koreaname2:

            results2=driver.find_element(By.ID,'ogIntro')
            Clicks_group2=results2.find_elements(By.CSS_SELECTOR,'.agent_site_info img')[Number_click] # 사이트 들어가기 
            # 사이트 클릭
            Clicks_group2.click() 
            Newresults=driver.find_element(By.ID,'ogIntro')
            # 신발이름
            Name_shoes=Newresults.find_element(By.CLASS_NAME,'page_title').text
            #신발 코드
            Code_shoes=Newresults.find_elements(By.CLASS_NAME,'product_info_data')[1].text
            # 신발가격
            price_shoes=Newresults.find_elements(By.CLASS_NAME,'product_info_data')[3].text
            
            # 동일한 신발 찾는거 피하기
            if Code_shoes not in Find_shoes:
                Find_shoes.append(Code_shoes)
                try:
                    # 미국 가격 적혀있는거 크림 사이트에서 가격 다시 가져오기
                    if 'USD' or 'EUR' in price_shoes:
                        
                        dis_price=int(10)

                    else:
                        # 원화는 WON제거만하기 
                        dis_price=re.findall("[0-9]*",price_shoes.strip())
                        dis_price="".join(dis_price)
                    
                        dis_price=int(dis_price)
                except:
                    pass
                # 링크가져오도록 작성
                Links_get=driver.find_element(By.CLASS_NAME,'site_card_layer')
                Links_pre=Links_get.find_elements(By.CLASS_NAME,'site_card')
                End_date=Links_get.find_elements(By.CLASS_NAME,'release_date_time')
                
                
                for Number in range(0,len(Links_pre)):
                    End_date=Links_get.find_elements(By.CLASS_NAME,'release_date_time')[Number].text
                    

                    if not End_date  == '종료': # 사이트에서 종료 라는 버튼이 있으면 안 가져오기
                        Site_Name=Links_get.find_elements(By.CLASS_NAME,'agent_site_title')[Number].text
                        # 한국이름만 필터링 해서 들어갈수 있도록
                        disting_site=re.findall("[가-힣]*[ ]*",Site_Name.rstrip())
                        disting_site2="".join(disting_site)
                        # if 문을 돌려서 사이트만 가져올수 있도록
                        if Site_Name in disting_site2:
                            Link_pre=Links_get.find_elements(By.CSS_SELECTOR,'.site_card a')[Number]
                            # 링크 가져오기
                            Link=Link_pre.get_attribute('href')
                            #임시 변수에 신발이름, 신발코드, 가격, 링크 넣어두기
                            Link_shoes.append(Link)
                                
                    else:  
                        pass
                
                
                temp=[Name_shoes,Code_shoes,dis_price,Link_shoes]
                # 크림에 보내줄 신발 Information_shoes리스트에 넣어두기
                Information_shoes.append(temp)
                
                
                            
                
            else:
                pass
        
            driver.back()
        else:
            pass

    # 외국 달러로 적혀있는거  def Change_price 돌려서 크림사이트에 있는 가격정보 가져오기
    for numq in range(0,len(Information_shoes)):
        if Information_shoes[numq][2] == 10:
            Information_shoes[numq][2]=int(Change_price(Information_shoes[numq][1]))
        else:
            pass
            
        # 크림 사이트
    URL='https://kream.co.kr/search?keyword='
    # 리셀 가격 5만원 이상인거 넣어둘 리스트
    Send_me=[]
    
    for information in Information_shoes:
        #가격 하고 신발 코드 없는거 걸러내기
        try:
            
            if information[1]=='-' or information[2]=='':
                pass
            else:
                # 찾고 싶은 신발 리셀 가격 찾기
                Base_URL=f'{information[1]}'
                driver.get(URL+Base_URL)
                result=driver.find_element(By.CLASS_NAME,'amount').text
                # 신발 가격만 나오도록 필터 
                filter_re=re.findall('[0-9]*',result)
                Final_re="".join(filter_re)

                Final_re=int(Final_re)
                Compare_pirce=Final_re-information[2]
                
                
                # 5만원 이상만 걸러내기
                if Compare_pirce> 50000:
                    
                    shoe=[information[0],str(f'{Compare_pirce:,}'),information[3]]
                    # send_me에 담아두기
                    Send_me.append(shoe)
        except:
            pass

    
    return Send_me  