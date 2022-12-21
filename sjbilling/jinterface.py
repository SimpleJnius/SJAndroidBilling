from jnius import PythonJavaClass, java_method


class ConsumeResponseListener(PythonJavaClass):
    __javainterfaces__ = ["com/android/billingclient/api/ConsumeResponseListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("(Lcom/android/billingclient/api/BillingResult;Ljava/lang/String;)V")
    def onConsumeResponseListener(self, billingResult, purchaseToken):
        self.callback(billingResult, purchaseToken)


class PurchaseHistoryResponseListener(PythonJavaClass):
    __javainterfaces__ = ["com/android/billingclient/api/PurchaseHistoryResponseListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("(Lcom/android/billingclient/api/BillingResult;Ljava/util/List;)V")
    def onPurchaseHistoryResponse(self, billingResult, purchasesHistoryList):
        self.callback(billingResult, purchasesHistoryList)


class PurchasesResponseListener(PythonJavaClass):
    __javainterfaces__ = ["com/android/billingclient/api/PurchasesResponseListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("(Lcom/android/billingclient/api/BillingResult;Ljava/util/List;)V")
    def onQueryPurchasesResponse(self, billingResult, purchases):
        self.callback(billingResult, purchases)


class PurchaseCanceledListener(PythonJavaClass):
    _javainterfaces__ = ["com/sj/sjgoogleplaybilling/PurchaseCanceledListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("(Lcom/android/billingclient/api/BillingResult;Ljava/util/List;)V")
    def onPurchaseCanceled(self, billingResult, purchases):
        self.callback(billingResult, purchases)


class PurchaseErrorListener(PythonJavaClass):
    _javainterfaces__ = ["com/sj/sjgoogleplaybilling/PurchaseErrorListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("(Lcom/android/billingclient/api/BillingResult;Ljava/util/List;)V")
    def onPurchaseError(self, billingResult, purchases):
        self.callback(billingResult, purchases)


class BillingServiceDisconnectedListener(PythonJavaClass):
    _javainterfaces__ = ["com/sj/sjgoogleplaybilling/PurchaseErrorListener"]

    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    @java_method("()V")
    def onBillingServiceDisconnected(self):
        self.callback()
