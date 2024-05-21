from service.display.screen import BaseScreen
from util import get_ellipsized_str, create_video_metadata_str, create_video_navigation_info_str, get_newline


class HomeScreen(BaseScreen):
    def render(self, data, menu_str):
        super().render(data, menu_str)

        screen_width = data.get('screen_width')

        if 'thumbnail' not in data.keys():
            self.write_to_screen('Could not load home screen.')
            return

        title = data['title']
        creator = data['creator']
        thumbnail = data['rendered_thumbnail']

        render_str = ''

        # Add nav controls info.
        render_str += create_video_navigation_info_str(screen_width)

        # Add thumbnail.
        render_str += thumbnail['content']

        if thumbnail['width'] > 5:
            # Add video title, ellipsized if necessary.
            render_str += f" {get_ellipsized_str(title, screen_width - 2)} {get_newline()}"

            # Add video metadata.
            render_str += create_video_metadata_str('', '', creator, screen_width)

        self.write_to_screen(render_str)
