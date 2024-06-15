from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.models import Order

def checkout(request, order_pk):
    try:
        order = get_object_or_404(Order, id=order_pk)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

    total_price = sum(item.product.price * item.quantity for item in order.items.all())
    total_price = float(f"{total_price:.2f}")

    return JsonResponse({"total_price": str(total_price)})
