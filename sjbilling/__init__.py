"""Google Play Billing

See the below links for detailed explanation:
    * https://developer.android.com/google/play/billing
    * https://developer.android.com/google/play/billing/integrate
    * https://medium.com/@patpatchpatrick/adding-the-google-play-billing-library-to-your-application-fbeb9ec03151

Basic usage:
    >>> from sjbilling import make_payment, PRODUCT_TYPE_INAPP
    >>> from kvdroid import activity
    >>> make_payment(activity.getApplicationContext(), activity, PRODUCT_TYPE_INAPP, "my_product_id")

Complex usage with some few listeners:
    >>> from sjbilling import make_payment, PRODUCT_TYPE_INAPP
    >>> from kvdroid import activity
    >>> callback = lambda billingResult, purchaseToken: print(billingResult, purchaseToken)
    >>> make_payment(activity.getApplicationContext(), activity, PRODUCT_TYPE_INAPP, "my_product_id", consume_response_listener=callback)

"""

from .jclass import SJGooglePlayBilling as Bill
from kvdroid.jclass.java import String
from .jinterface import ConsumeResponseListener, PurchaseHistoryResponseListener, PurchasesResponseListener, \
    PurchaseCanceledListener, PurchaseErrorListener, BillingServiceDisconnectedListener

_listeners = {
    "consume_response_listener": [ConsumeResponseListener, Bill.setConsumeResponseListener],
    "purchase_history_response_listener": [PurchaseHistoryResponseListener, Bill.setPurchaseHistoryResponseListener],
    "purchases_response_listener": [PurchasesResponseListener, Bill.setPurchasesResponseListener],
    "purchase_canceled_listener": [PurchaseCanceledListener, Bill.setPurchaseCanceledListener],
    "purchase_error_listener": [PurchaseErrorListener, Bill.setPurchaseErrorListener],
    "billing_service_disconnected_listener":
        [BillingServiceDisconnectedListener, Bill.setBillingServiceDisconnectedListener]

}

PRODUCT_TYPE_INAPP = "inapp"
PRODUCT_TYPE_SUBS = "subs"


class ListenerDoesNotExistException(Exception):
    pass


def make_payment(context: object, activity: object, product_type: str, product_id: str, **kwargs) -> object:
    """See module documentation for usage

    Parameters
    --------
    context: object
        The Application Context
    activity: object
        The current Application Activity
    product_type: str
        The type of purchases to be made (subscription or in-app purchases)
    product_id: str
        The ID of the product to be purchased. See In app product in play console
    kwargs:
        optional callable listeners for-->
        consume_response_listener: callback(billingResult, purchaseToken)
            called when the purchased product is consumed
        purchase_history_response_listener: callback(billingResult, purchasesHistoryList)
            called when getPurchaseHistory() of SJGooglePlayBilling returns the
            most recent purchase made by the user for each product,
            even if that purchase is expired, canceled, or consumed.
        purchases_response_listener: callback(billingResult, purchases)
            called when purchases has been made or not made due to network error
        purchase_canceled_listener: callback(billingResult, purchases)
            called when purchases has been cancelled by the user
        purchase_error_listener: callback(billingResult, purchases)
            called when error occurs during purchases
        billing_service_disconnected_listener: callback()
            called when billing services has disconnected

    Returns
    ------
    object
        returns billingResult


    """
    for listener, callback in kwargs.items():
        if listener not in _listeners:
            raise ListenerDoesNotExistException(f'Unknown {listener!r} listener')
        listener_interface = kwargs[listener][0]
        set_listener = kwargs[listener][1]
        set_listener(listener_interface(callback))
        return Bill.makePayment(context, activity, String(product_type), String(product_id))
