from django.test import TestCase
from ..models import Participants, EnvironmentExposures, GeneticMutations


class TestParticipantsGetExposures(TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_returns_empty_list(self):
        """
        Returns an empty list when there are no exposures
        """
        participant = Participants.objects.create(
            name="John", age="41", siblings=3)

        exposures = participant.get_exposures()
        self.assertEqual(exposures, [])

    def test_returns_exposure_names_as_list(self):
        """
        Returns a list of the names of the exposures associated with the participant
        """
        participant = Participants.objects.create(
            name="John", age="41", siblings=3)
        first_exposure = EnvironmentExposures.objects.create(name="First")
        second_exposure = EnvironmentExposures.objects.create(name="Second")

        participant.exposures.add(first_exposure)
        participant.exposures.add(second_exposure)

        exposures = participant.get_exposures()

        self.assertEqual(exposures, ['First', 'Second'])


class TestParticipantsGetMutations(TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_returns_empty_list(self):
        """
        Returns an empty list when there are no mutations
        """
        participant = Participants.objects.create(
            name="John", age="41", siblings=3)

        mutations = participant.get_mutations()
        self.assertEqual(mutations, [])

    def test_returns_mutation_names_as_list(self):
        """
        Returns a list of the names of the mutations associated with the participant
        """
        participant = Participants.objects.create(
            name="John", age="41", siblings=3)
        first_mutation = GeneticMutations.objects.create(name="First")
        second_mutation = GeneticMutations.objects.create(name="Second")

        participant.mutations.add(first_mutation)
        participant.mutations.add(second_mutation)

        mutations = participant.get_mutations()

        self.assertEqual(mutations, ['First', 'Second'])
