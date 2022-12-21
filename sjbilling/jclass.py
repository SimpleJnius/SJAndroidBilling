from jnius import autoclass, JavaClass, MetaJavaClass, JavaMethod
from kvdroid.jclass import _class_call


# def SJGooglePlayBilling(*args, instantiate: bool = False):
#     return _class_call(autoclass('com.sj.sjgoogleplaybilling.SJGooglePlayBilling'), args, instantiate)


class SJGooglePlayBilling(JavaClass, metaclass=MetaJavaClass):
    _javaclass__ = 'com/sj/sjgoogleplaybilling/SJGooglePlayBilling'

    makePayment = JavaMethod(
        "(Landroid/content/Context;Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)Lcom/android"
        "/billingclient/api/BillingResult;"
    )
    setConsumeResponseListener = JavaMethod("(Lcom/android/billingclient/api/ConsumeResponseListener;)V")
    setPurchasesResponseListener = JavaMethod("(Lcom/android/billingclient/api/PurchasesResponseListener;)V")
    setPurchaseHistoryResponseListener = JavaMethod(
        "(Lcom/android/billingclient/api/PurchaseHistoryResponseListener;)V"
    )
    getPurchaseHistory = JavaMethod("()V")
    setPurchaseCanceledListener = JavaMethod("(Lcom/sj/sjgoogleplaybilling/PurchaseCanceledListener;)V")
    setPurchaseErrorListener = JavaMethod("(Lcom/sj/sjgoogleplaybilling/PurchaseErrorListener;)V")
    setBillingServiceDisconnectedListener = JavaMethod(
        "(Lcom/sj/sjgoogleplaybilling/BillingServiceDisconnectedListener;)V"
    )



