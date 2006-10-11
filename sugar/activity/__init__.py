import gtk

from sugar.graphics.grid import Grid

settings = gtk.settings_get_default()

grid = Grid()
sizes = 'gtk-large-toolbar=%d, %d' % (grid.dimension(1), grid.dimension(1))
settings.set_string_property('gtk-icon-sizes', sizes, '')

settings.set_string_property('gtk-font-name', 'Sans 14', '')

def get_default_type(activity_type):
	"""Get the activity default type.

	   It's the type of the main network service which tracks presence
       and provides info about the activity, for example the title."""
	splitted_id = activity_type.split('.')
	splitted_id.reverse()
	return '_' + '_'.join(splitted_id) + '._udp'
