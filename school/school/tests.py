from django.test import TestCase
from .models import Class, Student


# Create your tests here.
class ClassTestCase(TestCase):
    def setUp(self):
        # Definir las clases del colegio de prueba
        class1 = Class.objects.create(floor='1', door='A')
        class2 = Class.objects.create(floor='2', door='B')

        # Definir los estudiantes del colegio
        student1 = Student.objects.create(name='student1')
        student2 = Student.objects.create(name='student2')

        #Asignar estos estudiantes a clases
        class1.students.add(student1)
        class2.students.add(student2)

    def test_attributes(self):
        # Obtener las dos clases de prueba
        class1 = Class.objects.get(id=1)
        class2 = Class.objects.get(id=2)

        # Comprobar que existen y que el método __str__ funciona correctamente
        self.assertEqual(str(class1), '1 - A')
        self.assertEqual(str(class2), '2 - B')

        # Obtener los estudiantes de esas clases y comprobar que existen
        student1 = class1.students.filter(name='student1')
        student2 = class2.students.filter(name='student2')
        self.assertIsNotNone(student1)
        self.assertIsNotNone(student2)
