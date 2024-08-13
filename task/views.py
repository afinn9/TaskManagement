from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AddSerializer
from .models import Task


@api_view(['GET'])
def view_task(request):
    data = Task.objects.all()
    serializer = AddSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def add_task(request):
    serializer = AddSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def edit_task(request, uuid):
    try:
        task_uuid = uuid
        new_name = request.data.get('name')

        if not new_name:
            return Response({'error': 'Missing name parameter'})

        # Fetch the task by UUID
        obj = Task.objects.get(uuid=task_uuid)
        obj.name = new_name
        obj.save()

        return Response({'message': 'Task updated successfully'})
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'})
    except Exception as e:
        return Response({'error': str(e)})


@api_view(['GET'])
def manage_task_state(request, uuid):
    obj = Task.objects.get(uuid=uuid)
    is_active_value = request.GET.get('is_active')
    is_active = is_active_value == 'true'
    print("sssssss", is_active_value)
    obj.is_active = is_active
    obj.save()
    return Response({'message': 'Updated successfully'})
