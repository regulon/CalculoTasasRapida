from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy import platform

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


class WebApp(App):

    def build(self):
        if platform == "android":
            self.open_webview()
        return BoxLayout()

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