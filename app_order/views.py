from django.http import Http404
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from .serializers import OrderSerializer
from .models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/order-list/',
        'Detail View': '/order-detail/<str:pk>/',
        'Order Create': 'order-create/',
        'Order Update': 'order-update/<str:pk>/',
        'Order Delete': 'order-delete/<str:pk>/',
    }
    return Response(api_urls)

class OrderList(APIView):
    def get(self, request):
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def orderDetail(request, pk):
    orders = Order.objects.get(id=pk)
    serializer = OrderSerializer(orders, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def orderCreate(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



class OrderUpdateView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if request.data['status_of_order'] == 'Created':
            if request.data['status_of_order'] == "Accepted" or request.data['status_of_order'] == "Cancelled":
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.error_messages('sorry \n Accept or Cancell'))
        elif request.data['status_of_order'] == 'Finished':
            return redirect('order-list')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order-list')








