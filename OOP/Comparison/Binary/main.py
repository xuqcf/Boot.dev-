can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    permission = can_create_guild & user_permissions
    return permission 


def get_review_bits(user_permissions):
    permission = can_review_guild & user_permissions
    return permission 


def get_delete_bits(user_permissions):
    permission = can_delete_guild & user_permissions
    return permission 


def get_edit_bits(user_permissions):
    permission = can_edit_guild & user_permissions
    return permission 
