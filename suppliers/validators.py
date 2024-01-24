from rest_framework.serializers import ValidationError


class DebtValidator:
    """Валидатор на запрет обновление задолженности"""

    def __init__(self, debt_field):
        self.debt_field = debt_field

    def __call__(self, value):
        debt = value.get(self.debt_field)

        if debt:
            raise ValidationError(
                'Стоит запрет на обновление задолженности перед поставщиком!'
            )
