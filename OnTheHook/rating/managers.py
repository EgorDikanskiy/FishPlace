from django.db import models
import rating.models

__all__ = []


class RatingManager(models.Manager):
    def marks(self, spot):
        return (
            super()
            .get_queryset()
            .select_related(
                "spot",
                "user",
            )
            .filter(spot=spot)
        )

    def user_marks(self, user):
        return (
            super()
            .get_queryset()
            .select_related("spot", "user")
            .filter(user=user)
            .order_by(
                "-created_at",
                "mark",
            )
        )

    def commets(self, pk):
        return (
            super()
            .get_queryset()
            .filter(
                spot_id=pk,
            )
            .select_related("user")
            .prefetch_related(
                models.Prefetch(
                    "rating_images",
                    queryset=rating.models.RatingImages.objects.only("image"),
                ),
            )
            .only(
                "user__username",
                "user__avatar",
                "mark",
                "comment",
                "created_at",
            )
        )
