from typing import Optional
import nextcord


class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
