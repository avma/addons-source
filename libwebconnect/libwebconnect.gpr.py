#------------------------------------------------------------------------
#
# Register the Addon
#
#------------------------------------------------------------------------

register(GENERAL,
         id="libwebconnect",
         name="libwebconnect",
         description = _("Library for web site collections"),
         status = STABLE, # not yet tested with python 3
         version = '1.0.34',
         gramps_target_version = "5.2",
         fname="libwebconnect.py",
         load_on_reg = True,
         )

