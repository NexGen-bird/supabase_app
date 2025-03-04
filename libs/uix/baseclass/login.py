from main_imports import MDScreen,MDDialog,dp,MDDialogHeadlineText,MDDialogSupportingText
from libs.applibs import utils
from supabase_lib.supabase_auth import login_with_email_password,send_password_reset_email
from kivy.core.window import Window

utils.load_kv("login.kv")

class Login_Screen(MDScreen):
    def on_enter(self):
        """
        This method used in development to avoid login 
        """
        pass
    def login(self, email, password):
        user = login_with_email_password(email, password)
        if user:
            self.auth_token = user.session.access_token
            # dialog = MDDialog(
            #     MDDialogHeadlineText(
            #     text="User Details",
            #     halign="left",
            # ),
            # MDDialogSupportingText(
            #     text=f"Welcome, User {user.user.email}!",
            #     halign="left",
            # ),
            # )
            # dialog.open()
            self.parent.change_screen("land")
            # self.on_login_success(user["email"])
        # else:
        #     utils.snack(color="red",text="Login failed. Please check your credentials.")

    def on_login_success(self, user_id):
        # Navigate to the next screen or perform other post-login actions
        utils.snack(color="green",text=f"Welcome, User {user_id}!")
        # Add logic here to navigate to the main screen or dashboard
    
    def forgot_password(self, email):
        if not email:
            utils.snack(color="red",text="Please enter your email address.")
        else:
            success = send_password_reset_email(email)
            if success:
                utils.snack(color="green",text="Password reset email sent! Check your inbox.")
            else:
                utils.snack(color="red",text="Failed to send password reset email.")