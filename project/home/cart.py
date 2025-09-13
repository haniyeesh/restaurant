from .models import CartItem,Cart


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key or request.session.save()
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

        
def add_to_cart(cart, food, quantity):
    cart_item, created = CartItem.objects.get_or_create(
        cart =cart,
        food= food,
    )
    if not created:
        cart_item.quantity += quantity
    else :
        cart_item.quantity = quantity
    cart_item.save()
    
def decrease_item(cart, food):
    try:
        cart_item, created = CartItem.objects.get_or_create(
        cart =cart,
        food= food
    )
        if cart_item.quantity > 1:
            cart_item.quantity -=1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
def get_cart_item(cart):
    return CartItem.objects.filter(cart=cart)


def calculate_total(cart):
    items = CartItem.objects.filter(cart=cart)
    return sum(item.food.price * item.quantity for item in items)