import pytest
from django.urls import reverse

from students.models import Course


@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-detail', args=(course[0].id,))
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['id'] == course[0].id
    assert response_json['name'] == course[0].name


@pytest.mark.django_db
def test_get_courses(api_client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == len(courses) == 10


@pytest.mark.django_db
def test_filter_course_by_id(api_client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = api_client.get(url, data={'id': courses[0].id})
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == 1
    assert response_json[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_filter_course_by_name(api_client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = api_client.get(url, data={'name': courses[0].name})
    response_json = response.json()
    assert response.status_code == 200
    assert response_json[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(api_client):
    count = Course.objects.count()
    url = reverse('courses-list')
    response = api_client.post(url, data={'name': 'Python'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert response.data['name'] == 'Python'


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-detail', args=(courses[0].id,))
    response = api_client.put(url, data={'id': '2', 'name': 'Python'})
    assert response.status_code == 200
    assert response.data['name'] == 'Python'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    url = reverse('courses-detail', args=(courses[0].id,))
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
