from ads.models import Ad
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad
