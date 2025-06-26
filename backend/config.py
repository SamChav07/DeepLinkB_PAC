import os

class Config:
    URL_BIBLIOTECA = "https://biblioteca.uam.edu.ni/intranet/"
    USUARIO = "22011319"
    PASSWORD = "420915"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    NOMBRE_GOOGLE_SHEET = "DeepLinkB_PAC"

    # Si vas a usar esto después
    MAPA_FACULTADES = {
        "fia": "Ingeniería y Arquitectura",
        "fcae": "Ciencias Administrativas y Económicas",
        "fcjhri": "Ciencias Jurídicas y Relaciones Internacionales",
        "fcm": "Ciencias Médicas",
        "fmdcc": "Marketing, Diseño^ y Ciencias de la Comunicación",
        "fodo": "Odontología",
        "lenguage center": "Inglés",
    }

    CATEGORIA_OPCIONES_WEB = {
        "Ingeniería y Arquitectura": {
            "McGraw Hill eBooks 7-24": "//img[contains(@src,'ebooks.jpg')]",
            "ARQUITECTURA VIVA": "//img[contains(@src,'arq.PNG')]",
            "EL CROQUIS": "//img[contains(@src,'elcro.PNG')]",
        },
        "Ciencias Administrativas y Económicas": {
            "McGraw Hill eBooks 7-24": "//img[contains(@src,'ebooks.jpg')]",
            "eLibro Colección Catedra": "//img[contains(@src,'elibro1.png')]",
            "DIGITALIA": "//img[contains(@src,'hispanica.PNG')]",
            "EBSCO": "//img[contains(@src,'ebsco.png')]",
            "Research4life": "//img[contains(@src,'R4L.jpg')]",
        },
        "Ciencias Jurídicas y Relaciones Internacionales": {
            "vLex Global": "//img[contains(@src,'vlex1.png')]",
            "GOALI": "//img[contains(@src,'goali.png')]",
        },
        "Ciencias Médicas": {
            "McGraw Hill Access Medicine": "//img[contains(@src,'McGrawHill1.gif')]",
            "HINARI": "//img[contains(@src,'hinari.png')]",
            "AMOLCA": "//img[contains(@src,'amolca.jpg')]",
            "Research4life": "//img[contains(@src,'R4L.jpg')]",
            "EBSCO": "//img[contains(@src,'ebsco.png')]",
        },
        "Marketing, Diseño y Ciencias de la Comunicación": {
            "eLibro Colección Catedra": "//img[contains(@src,'elibro1.png')]",
            "DIGITALIA": "//img[contains(@src,'hispanica.PNG')]",
            "EBSCO": "//img[contains(@src,'ebsco.png')]",
        },
        "Odontología": {
            "AMOLCA": "//img[contains(@src,'amolca.jpg')]",
            "HINARI": "//img[contains(@src,'hinari.png')]",
        },
        "Inglés": {
            "EBSCO": "//img[contains(@src,'ebsco.png')]",
            "DIGITALIA": "//img[contains(@src,'hispanica.PNG')]",
        },
        # "General": {
        #     "EBSCO": "//img[contains(@src,'ebsco.png')]",
        #     "eLibro Colección Catedra": "//img[contains(@src,'elibro1.png')]",
        #     "DIGITALIA": "//img[contains(@src,'hispanica.PNG')]",
        # },
        "General": {   #PREVENTIVA EN CASO QUE NO ENCUENTRE DE MANERA ADECUADA LA FACULTAD
            "McGraw Hill eBooks 7-24": "//img[contains(@src,'ebooks.jpg')]",
            "ARQUITECTURA VIVA": "//img[contains(@src,'arq.PNG')]",
            "EL CROQUIS": "//img[contains(@src,'elcro.PNG')]",
            "eLibro Colección Catedra": "//img[contains(@src,'elibro1.png')]",
            "DIGITALIA": "//img[contains(@src,'hispanica.PNG')]",
            "EBSCO": "//img[contains(@src,'ebsco.png')]",
            "Research4life": "//img[contains(@src,'R4L.jpg')]",
            "vLex Global": "//img[contains(@src,'vlex1.png')]",
            "GOALI": "//img[contains(@src,'goali.png')]",
            "McGraw Hill Access Medicine": "//img[contains(@src,'McGrawHill1.gif')]",
            "HINARI": "//img[contains(@src,'hinari.png')]",
            "AMOLCA": "//img[contains(@src,'amolca.jpg')]",
        },
    }

    CATALOGOS_FORMULARIOS = {
        "McGraw Hill Access Medicine": {
            "search_input_xpath": "//input[@id='txtSearchTerm-MicrositeHeroSearchNavBar']",
            "submit_xpath": "//input[@id='txtSearchTerm-MicrositeHeroSearchNavBar']",
            "submit_action": "enter",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "McGraw Hill eBooks 7-24": {
            "search_input_xpath": "xpath=//input[@id='SEARCH_opensearch-inputEl']",
            "submit_xpath": "xpath=//span[@id='button-1010-btnInnerEl']",
            "submit_action": "enter",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "vLex Global": {
            "search_input_xpath": "xpath=(//input[@id='search-query-input'])[2]",
            "submit_xpath": "xpath=(//input[@id='search-query-input'])[2]",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "EBSCO": {
            "search_input_xpath": "xpath=//input[@id='search-input",
            "submit_xpath": "css=.eb-search-button__icon",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "eLibro Colección Catedra": {
            "button_for_search_xpath": "xpath=//a[contains(text(),'Búsqueda Rápida')]",
            "search_input_xpath": "xpath=//input[@id='overlay-search']",
            "submit_xpath": "//button[@id='search-button']",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "HINARI": {
            "search_input_xpath": "xpath=//input[@name='q']",
            "submit_xpath": "xpath=//i[contains(.,'search')]",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "GOALI": {
            "search_input_xpath": "xpath=//input[@name='q']",
            "submit_xpath": "xpath=//i[contains(.,'search')]",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "AMOLCA": {
            "button_for_search_xpath": "css=.SearchBox-openBtn path:nth-child(1)",
            "search_input_xpath": "xpath=//input[@type='search']",
            "submit_xpath": "css=.SearchBox-submit svg",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "Research4life": {
            "search_input_xpath": "xpath=//input[@name='q']",
            "submit_xpath": "xpath=//i[contains(.,'search')]",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "DIGITALIA": {
            "search_input_xpath": "xpath=//input[@name='q0']",
            "submit_xpath": "xpath=//button[@id='go']/i",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",
        },
        "ARQUITECTURA VIVA": {
            "button_for_search_xpath": "css=.actions:nth-child(1) .js-main-search > .las",
            "search_input_xpath": "css=input:nth-child(1)",
            "submit_xpath": "css=.main-search__button > .las",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]",  # opcional, para validar resultado
        },
        "EL CROQUIS": {
            "search_input_xpath": "css=.home-searchbar > .show",
            "submit_xpath": "css=.icon",
            "submit_action": "click",  # puede ser "enter" o "click"
            "result_xpath": "//div[contains(@class, 'search-results')]", 
        },
    }