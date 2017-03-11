from django.contrib.staticfiles.storage import HashedFilesMixin
from whitenoise.storage import CompressedManifestStaticFilesStorage


class CustomCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    patterns = HashedFilesMixin.patterns + (
        ("scripts/app.js", (
            (r"""([{]{2}\s*ctrl.staticUrl.get\([\\]['"]{0,1}\s*(.*?)[\\]["']{0,1}\)\s*[}]{2})""",
             """{{ctrl.staticUrl.get(\\'%s\\')}}"""),
        )),
    )
