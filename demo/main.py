from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from sjbilling import make_payment, PRODUCT_TYPE_INAPP
from kvdroid import activity


class TestApp(App):
    def build(self):
        relative = RelativeLayout()
        relative.add_widget(
            Button(text="Make Payment", size=(.5, .3), pos_hint={"center": [.5, .5]}, on_release=self.pay))
        return relative

    @staticmethod
    def pay(*_):
        make_payment(activity.getApplicationContext(), activity, PRODUCT_TYPE_INAPP, "my_product_id")


TestApp().run()
