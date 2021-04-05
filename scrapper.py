from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import os
import youtube_dl


def getEpisodioLink(num_ep):

	print("\nA procurar o episódio "+str(num_ep)+" no Youtube...")
	driver_exe = 'chromedriver'
	options = Options()
	options.add_argument("--headless")
	driver = webdriver.Chrome(driver_exe, options=options)
	driver.get("https://www.youtube.com/results?search_query=Emanet+"+str(num_ep))
		
	time.sleep(2)

	button = driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div > div.NIoIEf > div.G4njw > div.qqtRac > form > div.lssxud > div > button')
	button.click()
	print("Episódio encontrado. A obter o link do episódio...")

	link = driver.find_element_by_xpath("//*[@id='video-title']").get_attribute('href')
	driver.close()
	print("--------------------------------------------------------------------")
	print("---           "+str(link)+"        ---")
	print("--------------------------------------------------------------------")

	return link

def downloadLegenda(link_epi):

	#driver_exe = 'chromedriver'
	#options = Options()
	#options.add_argument("--headless")
	driver = webdriver.Chrome()
	print("A procurar a legenda...")
	driver.get("https://savesubs.com/process?url="+link_epi)
	driver.minimize_window()

	time.sleep(5) 
	select = Select(driver.find_element_by_name('slang'))
	select2 = Select(driver.find_element_by_name('tlang'))

	from_language = "tr"
	to_language = "pt"

	if alterar_lingua=="n":
		options_from = driver.find_element_by_name('slang')
		options_from_list = [x for x in options_from.find_elements_by_tag_name("option")]
		options_to = driver.find_element_by_name('tlang')
		options_to_list = [x for x in options_to.find_elements_by_tag_name("option")]
		print("\n Original: ")

		for element in options_from_list:
			print(element.get_attribute("value"))

		print("\nTraduzida: ")
		
		for element2 in options_to_list:
			print(element2.get_attribute("value"))

		from_language = input("\nEscolha a linguagem orginal: ")
		to_language = input("\nEscolha a linguagem a traduzir: ")

	select.select_by_value(from_language)
	select2.select_by_value(to_language)	

	button = driver.find_element_by_css_selector('.lg\:w-1\/2 > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > button:nth-child(9)')
	button.click()
	print("Legenda encontrada. A descarregar...")
	name = driver.find_element_by_css_selector("#root > div > div > main > h2").text
	episodio=name[7:10]
	#asuccess
	episodio=episodio.replace(".","")
	episodio=episodio.replace(" ","")
	num_ep=episodio
	time.sleep(5) 
	driver.close()
	print("Legenda descarregada!")
	print("A enviar a legenda para a pasta selecionada...")

	print("\n---------------------------- Pronto! :) ----------------------------")

	prev_name="Emanet "+num_ep+". Bölüm _ Legacy Episode "+num_ep+" - Portuguese"
	new_name="Emanet "+num_ep+". Bölüm   Legacy Episode "+num_ep
	prev_path="/home/filipaze/Downloads/"+prev_name+".srt"
	new_path=download_folder+new_name+".srt"
	os.rename(prev_path,new_path)

def renameLegenda(lin):
	if lin=="zu":
		return "Zulu"

def downloadVideoAuto(link_epi):

	#driver_exe = 'chromedriver'
	#options = Options()
	#options.add_argument("--headless")
	#driver = webdriver.Chrome(driver_exe, options=options)
	driver = webdriver.Chrome()
	print("A iniciar o download do episódio...")
	driver.get("https://yt1s.com/pt1")
	driver.minimize_window()
	time.sleep(2)
	link_video = driver.find_element_by_name("q")
	link_video.send_keys(link_epi)
	
	button = driver.find_element_by_css_selector('#search-form > button')
	button.click()
	time.sleep(2)
	button = driver.find_element_by_css_selector('#btn-action')
	button.click()
	time.sleep(5)
	name = driver.find_element_by_css_selector("#asuccess").get_attribute('href')
	time.sleep(1)
	driver.close()
	#driver_exe = 'chromedriver'
	#options = Options()
	#options.add_argument("--headless")
	#driver = webdriver.Chrome(driver_exe, options=options)
	driver = webdriver.Chrome()
	driver.get(name)
	driver.minimize_window()
	print("Faltam 5 minutos...")
	time.sleep(60)
	print("Faltam 4 minutos...")
	time.sleep(60)
	print("Faltam 3 minutos...")
	time.sleep(60)
	print("Faltam 2 minutos...")
	time.sleep(60)
	print("Falta 1 minuto...")
	time.sleep(60)
	driver.close()


def downloadVideoManual(link_epi):

	print("O browser será aberto!\n")
	driver = webdriver.Chrome()
	print("A iniciar o download do episódio...")
	driver.get("https://yt1s.com/pt1")
	time.sleep(2)
	link_video = driver.find_element_by_name("q")
	link_video.send_keys(link_epi)
		
	button = driver.find_element_by_css_selector('#search-form > button')
	button.click()
	time.sleep(4)
	button = driver.find_element_by_css_selector('#btn-action')
	button.click()
	time.sleep(5)
	name = driver.find_element_by_css_selector("#asuccess").get_attribute('href')
	time.sleep(1)
	driver = webdriver.Chrome()
	driver.get(name)
	pronto=input("Quando o download terminar introduza 'p' e dê ENTER! ")

	if pronto=="p":
		driver.close()
		if opcao != 2 and opcao != 4 and opcao !=5:
			print("\nSucesso! Episódio "+str(i)+" pronto para assistir! :)")


# Menu
print("\n© Filipe Azevedo")
print("Download de legendas do Youtube!")
print("\nSites utilizados:")
print("savesubs.com")
print("youtube.com")


# Escolha de opções
opcao = int(input("\n(0) - Automático Legenda + Video "
					"\n(1) - Automático Legenda + Video Manual "
					"\n(2) - Lista.txt Legenda + Video Manual"
					"\n(3) - Automático Legenda"
					"\n(4) - Lista.txt Legenda + Video Automático"
					"\n(5) - Lista.txt Legenda"
					"\nEscolha uma opção: "))

if opcao!=2 and opcao != 4 and opcao != 5:

	min = input("Transferir do episodio: ")
	max = input("Até: ")
	episodios_total=int(max)-int(min)+1
	i=int(min)

download_folder="/home/filipaze/Documents/Emanet/"

escolha_pasta=input("\nA pasta de destino dos ficheiros está definida em "+download_folder+".\nPode ser? Sim(s) ou Não(n)? ")

if escolha_pasta=="n":

	download_folder=input("\nInsira o novo caminho no formato /xx/xx/xx/: ")


alterar_lingua = input("\nAs legendas estão em TURCO e serão traduzidas para PORTUGUÊS.\nEstá correto? Sim(s) ou Não(n)? ")
print("\n--------------------------   A iniciar   ---------------------------")
link_episodio=None



if opcao == 0:

	while i >=int(min) and i<=int(max):

		link_episodio = getEpisodioLink(i)
		try:
			downloadLegenda(link_episodio)
		except:
			print("\nO download da legenda do episódio "+str(i)+" deu erro. O video será descarregado na mesma\n")
			downloadVideoAuto(link_episodio)

		downloadVideoAuto(link_episodio)

		i=i+1

elif opcao == 1:	

	while i >=int(min) and i<=int(max):

		link_episodio = getEpisodioLink(i)
		try:
			downloadLegenda(link_episodio)
		except:
			print("\nO download da legenda do episódio "+str(i)+" deu erro. O video será descarregado na mesma\n")

		downloadVideoManual(link_episodio)

		i=i+1

	print("\nDescarregados video e legendas de "+str(episodios_total)+" episódios com sucesso!\n")

elif opcao == 2 or opcao == 4 or opcao == 5:

	with open('links.txt') as my_file:
		links = my_file.readlines()

	for x in links:	

		x=x[0:43]
		try:
			downloadLegenda(x)
		except:
			print("\nO download da legenda do episódio falhou. \n")
		
		if opcao == 2:
			downloadVideoManual(x)
		if opcao == 4:
			downloadVideoAuto(x)

	print("\nDescarregados video e legendas de "+str(len(links))+" episódios com sucesso!\n")

elif opcao == 3:

	erros=0
	while i >=int(min) and i<=int(max):

		link_episodio = getEpisodioLink(i)
		try:
			downloadLegenda(link_episodio)
		except:
			print("\nOps! O download da legenda do episódio "+str(i)+" falhou.")
			print("--------------------------------------------------------------------")
			link_episodio = getEpisodioLink(i+1)
			erros=erros+1
			i=i+1
			downloadLegenda(link_episodio)

		i=i+1

	if (episodios_total)!=1:

		print("\nDescarregadas "+str(episodios_total-erros)+" legendas com sucesso!\n")

	else:
		print("\nDescarregada 1 legenda com sucesso!\n")
		

elif opcao!=0 and opcao!=1 and opcao!=2 and opcao!=3:

	print("Opção não existe!")






