
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg


driver = webdriver.Edge()
driver.implicitly_wait(1)
#58
pagelist = [ 'https://www.deviantart.com/super-adopt-shop/gallery/', 
            'https://www.deviantart.com/all-art-of-creation/gallery/',
           'https://www.deviantart.com/discoverarts/gallery/',
           'https://www.deviantart.com/paypalcommissions/gallery/',
           'https://www.deviantart.com/u-buy-please/gallery/',
           'https://www.deviantart.com/adopt-shelter/gallery/',
           'https://www.deviantart.com/adoptia/gallery/',
           'https://www.deviantart.com/adoptswonderlandd/gallery/',
           'https://www.deviantart.com/adopt-oasis/gallery/',
           'https://www.deviantart.com/zee-adopts/gallery/',
           'https://www.deviantart.com/adoptababes/gallery/',
           'https://www.deviantart.com/adopt-an-adoptable/gallery/',
           'https://www.deviantart.com/adoptable-oc/gallery/',
           'https://www.deviantart.com/adoptable-batch/gallery/',
           'https://www.deviantart.com/admirableadoptables/gallery/',
           'https://www.deviantart.com/all-adopt-adoptable/gallery/',
           'https://www.deviantart.com/art--is--love/gallery/',
           'https://www.deviantart.com/adoptdesignhub/gallery/',
           'https://www.deviantart.com/adoptable-frenzy/gallery/',
           'https://www.deviantart.com/rainbow-adoptables/gallery/',
           'https://www.deviantart.com/paypaladoptioncenter/gallery/',
           'https://www.deviantart.com/humanoid-adopts/gallery/',
           'https://www.deviantart.com/growing-adoptables/gallery/',
           'https://www.deviantart.com/delightful-adopts/gallery/',
           'https://www.deviantart.com/more-adoptables/gallery/',
           'https://www.deviantart.com/adoption-city/gallery/',
           'https://www.deviantart.com/teamadoptables/gallery/',
           'https://www.deviantart.com/adoptik/gallery/',
           'https://www.deviantart.com/any-adoptables/gallery/',
           'https://www.deviantart.com/adorableadopts/gallery/',  
           'https://www.deviantart.com/adoptableshouse/gallery/',
           'https://www.deviantart.com/cutiessadopts/gallery/',
           'https://www.deviantart.com/adopts-all-around/gallery/',
           'https://www.deviantart.com/adopttoday/gallery/',
           'https://www.deviantart.com/adopts-wonderland/gallery/',
           'https://www.deviantart.com/adopt-commish-shop/gallery/',
           'https://www.deviantart.com/adopt-village/gallery/',
           'https://www.deviantart.com/adopt-awesomely/gallery/',
           'https://www.deviantart.com/adopt-to-ya-drop/gallery/',
           'https://www.deviantart.com/drawing-club02/gallery/',
           'https://www.deviantart.com/art-adoptables/gallery/',
           'https://www.deviantart.com/dasadoptablemachine/gallery/',
           'https://www.deviantart.com/yay-adopts/gallery/',
           'https://www.deviantart.com/adoptablemarketplace/gallery/',
           'https://www.deviantart.com/themedadoptables/gallery/',
           'https://www.deviantart.com/stardust-adoptable/gallery/',
           'https://www.deviantart.com/the-adoption-centre/gallery/',
           'https://www.deviantart.com/adoptable-farm/gallery/',
           'https://www.deviantart.com/shoppableadoptable/gallery/',
           'https://www.deviantart.com/celestialadoptcenter/gallery/',
           'https://www.deviantart.com/adoptshies/gallery/',
           'https://www.deviantart.com/unpopular-adoptables/gallery/',
           'https://www.deviantart.com/sugarcandykawaii/gallery/',
           'https://www.deviantart.com/ooadoptablesoo/gallery/',
           'https://www.deviantart.com/th-adoptable/gallery/',
           'https://www.deviantart.com/all-deviantarts-art/gallery/',
           'https://www.deviantart.com/rainbowadoptables/gallery/',
           'https://www.deviantart.com/auction-adoptables/gallery/']
wish = [
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[30]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[20]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[35]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[39]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[31]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[20]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[22]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[36]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[50]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[53]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[39]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[25]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]','//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[19]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[23]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[24]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[25]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[26]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[19]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[20]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[22]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[23]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[31]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[22]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[20]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[22]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[23]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[26]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[27]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]'],
           [],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[23]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[26]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[27]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[19]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[30]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[31]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[32]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[33]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[34]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[40]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[41]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[42]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[43]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[44]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[45]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[52]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]','//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[20]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[29]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[30]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[22]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[10]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[15]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[16]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[17]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[5]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[14]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[18]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[21]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[1]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[2]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[4]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[9]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[11]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]'],
           [],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[3]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[6]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]'],
           ['//*[@id="deviantART-v7"]/div[1]/div/div/div/div[7]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[8]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[12]', '//*[@id="deviantART-v7"]/div[1]/div/div/div/div[13]'],
       ]
global i
i= 0
def something():
    global i
    driver.get(pagelist[i])
    driver.implicitly_wait(4)
    contribute = driver.find_element(By.XPATH , '//*[@id="gmi-GalleryEditor"]/div[1]/div/div[1]/a') #Contribute
    contribute.click()
    driver.implicitly_wait(4)
    driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]').click() #select pic
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[1]/div[1]/div[2]/div/div').click() #폴더 목록 열기
    #---------------------위시리스트----------------------------------------------
    for c in range(0, len(wish[i])):
        driver.find_element(By.XPATH, wish[i][c] ).click() #원하는거 누르자
        driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[3]/table/tbody/tr/td[2]/a').click() #써브밋
        driver.implicitly_wait(0.0001)
        err = pg.locateCenterOnScreen('err.png', confidence = 0.8) #check submitted?
        acc = pg.locateCenterOnScreen('acc.png', confidence = 0.8) #check submitted?
        if acc != None: #판정
           print('찾음')
           ok()
           break
        elif err != None:
           print('이미 냄')
           ok()
           break
        else: #계속 찾겠다
           print('.')
           driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[1]/div[1]/div[2]/div/div').click() #폴더 목록 열기
    all()
    
def ok():
    global i
    i=i+1 #원하는거 찾음
    if i == len(pagelist): #fin
        driver.get('https://www.deviantart.com/all-art-4-ever/gallery/')
        driver.find_element(By.XPATH , '//*[@id="gmi-GalleryEditor"]/div[1]/div/div[1]/a').click()
        driver.implicitly_wait(4)
        driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]').click()
        driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[3]/table/tbody/tr/td[2]/a').click()
        print('end')
        driver.quit()
    else:
        something()

    #---------------------전수조사------------------------------------------------
def all():
    global i
    option = driver.find_elements(By.CLASS_NAME ,'option') #옵션들 찾기
    driver.implicitly_wait(2)
    for a in range(1, len(option)):
        option[a].click() #첫번째 옵션 선택
        driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[3]/table/tbody/tr/td[2]/a').click() #써브밋
        driver.implicitly_wait(0.0001)
        err = pg.locateCenterOnScreen('err.png', confidence = 0.8) #check submitted?
        acc = pg.locateCenterOnScreen('acc.png', confidence = 0.8) #check submitted?
        if acc != None: #판정
           print('찾음')
           break
        elif err != None:
           print('이미 냄')
           break
        else: #계속 찾겠다
           print('.')
           driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[1]/div[1]/div[2]/div/div').click() #폴더 목록 열기
    i=i+1 #다음 페이지
    if i == len(pagelist): #fin
        driver.get('https://www.deviantart.com/all-art-4-ever/gallery/')
        driver.find_element(By.XPATH , '//*[@id="gmi-GalleryEditor"]/div[1]/div/div[1]/a').click()
        driver.implicitly_wait(4)
        driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]').click()
        driver.find_element(By.XPATH ,'//*[@id="modalspace"]/div/div/div/div/div[3]/table/tbody/tr/td[2]/a').click()
        print('end')
        driver.quit()
    else:
        something()

def login():
     driver.get(pagelist[0])
     driver.implicitly_wait(4)
     driver.find_element(By.XPATH , '//*[@id="da-legacy-header"]/div/header/div[3]/a[2]/span').click()
     driver.implicitly_wait(2)
     driver.find_element(By.XPATH , '//*[@id="username"]').send_keys('po5po')
     driver.find_element(By.XPATH , '//*[@id="password"]').send_keys('!2629700go')
     driver.find_element(By.XPATH , '//*[@id="loginbutton"]').click()

login()
something()






