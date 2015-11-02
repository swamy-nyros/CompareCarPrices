from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.http import HttpResponse

from .models import Car_Master_Data,CarDetails

def master_data(request):

	city_id = ['105','2','12','3000','176','198','128','10','224','244']
	cities=['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'Delhi','Noida','Chandigarh']
	city_name = dict(zip(city_id,cities))

	make_id = ['10','8','20','16','17','7','5','2','9','15']
	makes=['Maruti Suzuki','Hyundai','Volkswagen','Tata','Toyota','Honda','Ford','Chevrolet','Mahindra','Skoda']
	makes_name = dict(zip(make_id,makes))

	Maruti_models_id = ['10.24','10.41','10.35','10.288','10.332']
	Maruti_models_name=['800','A-Star','Alto','Swift','Zen']
	Maruti = dict(zip(Maruti_models_id,Maruti_models_name))

	Hyundai_models_id=['8.307','8.31','8.113','8.261','8.278']
	Hyundai_models_name=['Verna','Accent','Elantra','Santro','Sonata']
	Hyundai = dict(zip(Hyundai_models_id,Hyundai_models_name))

	Volkswagen_models_id=['20.304','20.227','20.177','20.224']
	Volkswagen_models_name=['Vento','Polo','Jetta,Passat']
	Volkswagen = dict(zip(Volkswagen_models_id,Volkswagen_models_name))

	Tata_models_id=['16.169','16.169','16.257','16.213','16.193']
	Tata_models_name = ["Indica","Indigo","Safari","Nano","Manza"]
	Tata = dict(zip(Tata_models_id,Tata_models_name))

	Toyota_models_id=['17.172','17.135','17.88','17.353','17.58']
	Toyota_models_name = ['Innova','Fortuner','Corolla','Corolla Altis','Camry']
	Toyota = dict(zip(Toyota_models_id,Toyota_models_name))

	Honda_models_id=['7.32','7.36','7.74','7.75','7.98']
	Honda_models_name=['Accord','Amaze','City','Civic','CR-V']
	Honda = dict(zip(Honda_models_id,Honda_models_name))

	Ford_models_id=['5.111','5.114','5.128','5.166','5.141']
	Ford_models_name=['Ecosport','Endeavour','Fiesta','Ikon','Fusion']
	Ford = dict(zip(Ford_models_id,Ford_models_name))

	Chevrolet_models_id=['2.46','2.299','2.60','2.115','2.279']
	Chevrolet_models_name=['Aveo','Aveo U-Va','Captiva','Enjoy','Spark']
	Chevrolet = dict(zip(Chevrolet_models_id,Chevrolet_models_name))

	Mahindra_models_id=['9.53','9.174','9.266','9.236','9.328']
	Mahindra_models_name=['Bolero','Jeep','Scorpio','Quanto','Xylo']
	Mahindra = dict(zip(Mahindra_models_id,Mahindra_models_name))

	Skoda_models_id=['15.126','15.184','15.215','15.287','15.241']
	Skoda_models_name=['Fabia','Laura','Octavia','Superb','Rapid']
	Skoda = dict(zip(Skoda_models_id,Skoda_models_name))

	for key,values in city_name.items():
		city_id=key
		city_name=values
		print city_name
		for key,values in makes_name.items():
			make_id=key
			make_name=values
			print make_name
			if make_name == "Maruti Suzuki":
				for key,values in Maruti.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Hyundai":
				for key,values in Hyundai.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Volkswagen":
				for key,values in Volkswagen.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Tata":
				for key,values in Tata.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Toyota":
				for key,values in Toyota.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Honda":
				for key,values in Honda.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Ford":
				for key,values in Ford.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Chevrolet":
				for key,values in Chevrolet.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Mahindra":
				for key,values in Mahindra.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
			elif make_name == "Skoda":
				for key,values in Skoda.items():
					data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()

	return HttpResponse("master data of carwale stored into the database successfully")

def scrollDown(driver, numberOfScrollDowns):
	body = driver.find_element_by_tag_name("body")
	while numberOfScrollDowns >=0:
		body.send_keys(Keys.PAGE_DOWN)
		numberOfScrollDowns -= 1
	return driver



def carwale(request):
	driver = webdriver.Firefox()
	all_cars = Car_Master_Data.objects.all()
	for car in all_cars:
		driver.get("http://www.carwale.com/used/cars-for-sale/")
		print driver.title
		time.sleep(2)
		car_city = car.city_id
		car_make = car.make_id
		car_model = car.model_id
		city_name=car.city_name
		make_name=car.make_name
		model_name=car.model_name
		city = driver.find_element_by_css_selector('select#drpCity.form-control option[value="%s"]'%car_city)
		city.click()
		print city_name
		time.sleep(2)
		make = driver.find_element_by_css_selector("ul#makesList.ul-makes li.us-sprite.makeLi[carfilterid='%s']"%car_make) 
		make.click()
		print make_name
		time.sleep(10)
		model = driver.find_element_by_css_selector('ul#makesList.ul-makes li.us-sprite.makeLi div.list-points-models ul.rootUl li.us-sprite.rootLi[carfilterid="%s"]'%car_model)
		model.click()
		print model_name
		time.sleep(2)
		print '********cardata****'
		driver = scrollDown(driver, 2)
		car_data_list = [element for element in driver.find_elements_by_css_selector('div.stock-list ul#listing1.ko-listing li.listing-adv.listingContent.padding-top10.padding-bottom10.cur-pointer div.stock-detail')]		
		print "*********"*12
		print city_name
		time.sleep(2)
		for data in car_data_list:
			price = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 span.rupee-lac.slprice.font20').text
			print price
			time.sleep(2)

			title= data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').text
			print title

			href = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').get_attribute("href")
			print href
			time.sleep(5)

			driver = scrollDown(driver, 2)
			print"scroll"

			image = data.find_element_by_css_selector('div.leftfloat.thumb-div div.thumb-area div.img-placer a.slideShow img').get_attribute("src")
			print image

			year = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 a.text-grey p.listingItemKms.font14.text-light-grey.margin-top5 span:nth-of-type(7)').text
			print year

			time.sleep(2)
			CarDetails(website_name="www.carwale.com",
				city=city_name,
				car_make=make_name,
				car_model=model_name,
				price=price,
				model_year=year,
				car_title=title,
				car_href=href,
				car_image =image,
				).save()
						

	return HttpResponse("carwale data stored into the database successfully")

	
	
	