import wixData from 'wix-data';
import {fetch} from 'wix-fetch';
import wixSecretsBackend from 'wix-secrets-backend';

export async function wixStores_onNewOrder(event) {
    const secret = await wixSecretsBackend.getSecret("frontpad_API_key");
    const url = "https://app.frontpad.ru/api/index.php?new_order";
    const newOrderId = event.orderId;
    // Get the new order's line items from the Stores/Orders collection
    const order = await wixData.get("Stores/Orders", newOrderId);
    const { product, product_kol } = order.lineItems.reduce(({ product, product_kol }, { sku, quantity }) => ({
        product: [...product, sku],
        product_kol: [...product_kol, quantity]
    }), {product_kol: [], product: []})
    const data = {
        secret,
        product,
        product_kol,
        phone: order.shippingInfo.shipmentDetails.phone,
        mail: order.shippingInfo.shipmentDetails.email,
        name: order.shippingInfo.shipmentDetails.firstName + ' ' + order.shippingInfo.shipmentDetails.lastName,
        descr: "Заказ на сайте: #" + order.number + '; ' + (order.buyerNote ? order.buyerNote : ''),
        street: order.shippingInfo.shipmentDetails.address.city + ', ' + order.shippingInfo.shipmentDetails.address.addressLine,
        channel: 945,
        affiliate: 132,
    }
    var strData = [];
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            if (Array.isArray(data[key])) {
                strData.push(data[key].map((el, idx) => encodeURIComponent(key) + '[' + idx + ']=' + encodeURIComponent(el)).join('&'))
            } else {
                strData.push(encodeURIComponent(key) + "=" + encodeURIComponent(data[key]))
            }
        }
    }
    const result = await fetch(url, {
        method:"POST",
        body: strData.join("&"),
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
    });
}



