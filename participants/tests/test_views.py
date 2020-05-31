from django.test import TestCase
from ..models import Participants, EnvironmentExposures, GeneticMutations


class ParticipantListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        participant = Participants.objects.create(
            name="John", age="41", siblings=3)

        first_exposure = EnvironmentExposures.objects.create(name="First")
        second_exposure = EnvironmentExposures.objects.create(name="Second")

        first_mutation = GeneticMutations.objects.create(name="First")
        second_mutation = GeneticMutations.objects.create(name="Second")

        participant.exposures.add(first_exposure)
        participant.exposures.add(second_exposure)

        participant.mutations.add(first_mutation)
        participant.mutations.add(second_mutation)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/participants/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/participants/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'participants.html')

    def test_lists_all_authors(self):
        response = self.client.get('/participants/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['participants']) == 1)

        participant = response.context['participants'][0]
        self.assertTrue(participant.name, 'John')
