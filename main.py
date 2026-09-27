from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform

import os
import openpyxl

# Dirección de tu aplicación web en Streamlit Cloud
URL_STREAMLIT = "https://calculotasasrapida-deposito.streamlit.app/"

if platform == "android":
    from android.runnable import run_on_ui_thread
    from jnius import autoclass

    WebView = autoclass("android.webkit.WebView")
    WebViewClient = autoclass("android.webkit.WebViewClient")
    WebSettings = autoclass("android.webkit.WebSettings")
    CookieManager = autoclass("android.webkit.CookieManager")
    activity = autoclass("org.kivy.android.PythonActivity").mActivity
else:
    # Decorador neutro para pruebas fuera de Android
    def run_on_ui_thread(func):
        return func

    # Variables asignadas a None para evitar NameError en Windows
    WebView = None
    WebViewClient = None
    WebSettings = None
    CookieManager = None
    activity = None


class WebApp(App):

    def build(self):
        if platform == "android":
            self.open_webview()
            return BoxLayout()
        else:
            # En Windows muestra una interfaz de prueba para confirmar que el código funciona
            layout = BoxLayout(orientation='vertical')
            layout.add_widget(
                Label(text=f"Modo Escritorio ({platform})\nCargando URL:\n{URL_STREAMLIT}")
            )
            return layout

    @run_on_ui_thread
    def open_webview(self):
        if platform == "android":
            webview = WebView(activity)
            settings = webview.getSettings()
            
            # Configuraciones necesarias para el renderizado de Streamlit
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setDatabaseEnabled(True)
            settings.setAllowFileAccess(True)
            settings.setMixedContentMode(0)

            # Manejo de cookies
            cookie_manager = CookieManager.getInstance()
            cookie_manager.setAcceptCookie(True)
            cookie_manager.setAcceptThirdPartyCookies(webview, True)

            webview.setWebViewClient(WebViewClient())
            webview.loadUrl(URL_STREAMLIT)
            activity.setContentView(webview)


if __name__ == "__main__":
    WebApp().run()