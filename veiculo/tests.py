from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from veiculo.models import Veiculo
from veiculo.forms import *

class TestesModelVeiculo(TestCase):
    # Cria uma instância a ser testada
    def setUp(self):
        self.instancia = Veiculo(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3,
        )

    def test_is_new(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)

    def test_years_use(self):
        self.instancia.ano = datetime.now().year - 10
        self.assertEqual(self.instancia.anos_de_uso(), 10)

class TesteViewListarVeiculos(TestCase):
    # Cria instância de usuário e força login
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculo')
        Veiculo(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=2).save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('veiculos')), 1)

class TesteViewCriarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculo')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_post(self):
        data = {'marca' : 1, 'modelo': 'ABCDE', 'ano': 2, 'combustivel': 3, 'cor': 2}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculo'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'ABCDE')

class TesteViewEditarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=3)
        self.url = reverse('editar-veiculos', kwargs={'pk' : self.instancia.id})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.id)
        self.assertEqual(response.context.get('object').marca, self.instancia.marca)
    
    def test_post(self):
        data = {'marca' : 5, 'modelo': 'ASASNEGRAS', 'ano': 2, 'combustivel': 3, 'cor': 2}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculo'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 5)
        self.assertEqual(Veiculo.objects.first().pk, self.instancia.id)

class TesteViewDeletarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste', password='1')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=3)
        self.url = reverse('deletar-veiculos', kwargs={'pk' : self.instancia.id})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').marca, self.instancia.marca)

    def test_post(self):
        data = {'marca' : 5, 'modelo': 'ASASNEGRAS', 'ano': 2, 'combustivel': 3, 'cor': 2}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculo'))
        self.assertEqual(Veiculo.objects.count(), 0)