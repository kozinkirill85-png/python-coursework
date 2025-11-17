class LogCreationMixin:
    """Миксин для логирования создания объекта"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # ✅ Это важно!
        print(f"{self.__class__.__name__}({', '.join(map(str, args))})")