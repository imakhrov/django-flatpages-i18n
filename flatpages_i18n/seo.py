from djangoseo import seo


class FlatpagesMetadata(seo.Metadata):
    title        = seo.Tag(head=True, max_length=200)
    description  = seo.MetaTag(max_length=300)
    keywords     = seo.KeywordTag()
    heading      = seo.Tag(name="h1")

    class Meta:
        seo_models = ('flatpages_i18n', )
        seo_views = ('flatpages_i18n', )
        use_i18n = True

