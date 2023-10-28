from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Candiadate(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.IntegerField()
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="app/images/Candidate")


class AddmissionForm(models.Model):
        user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
        merit_no = models.IntegerField()
        mht_cet = models.IntegerField()
        seat_no_hsc = models.IntegerField()
        marks_hsc = models.IntegerField()
        percentage_hsc = models.IntegerField()
        name_of_board = models.CharField(max_length=50)
        prev_clg_name = models.CharField(max_length=50)
        stud_photo = models.ImageField(upload_to="app/images/Candidate")
        sign_photo = models.ImageField(upload_to="app/images/Candidate")

        name = models.CharField(max_length=50)
        surname = models.CharField(max_length=50)
        fathers_name = models.CharField(max_length=50)
        mothers_name = models.CharField(max_length=50)
        parents_full_name = models.CharField(max_length=50)
        paddress = models.CharField(max_length=80)
        pstate = models.CharField(max_length=50)
        pdistrict =models.CharField(max_length=50)
        ppincode = models.IntegerField()
        occupation = models.CharField(max_length=50)
        yearly_income = models.IntegerField()
        pmobile = models.IntegerField()

        laddress = models.CharField(max_length=100)
        lstate = models.CharField(max_length=50)
        ldistrict =models.CharField(max_length=50)
        lpincode = models.IntegerField()

        stud_email = models.CharField(max_length=50)

        stud_mob = models.IntegerField()

        place_of_birth = models.CharField(max_length=50)

        nationality = models.CharField(max_length=50)

        mhstate = models.CharField(max_length=50)

        religion = models.CharField(max_length=50)

        category =models.CharField(max_length=50)

        cast = models.CharField(max_length=50)

        pcm_mrks = models.IntegerField()

        phy_mrks =models.IntegerField()
        chem_mrks = models.IntegerField()
        maths_mrks = models.IntegerField()
        other_mrks = models.IntegerField()

        total_fees = models.IntegerField()
        recipt_no = models.IntegerField()

        adhar_no = models.IntegerField()
        pan_no = models.IntegerField()

        s_board = models.CharField(max_length=50)
        s_year_of_passing = models.IntegerField()
        s_mrks = models.IntegerField()
        s_outof = models.IntegerField()
        s_percentage = models.IntegerField()

        h_board = models.CharField(max_length=50)
        h_year_of_passing = models.IntegerField()
        h_mrks = models.IntegerField()
        h_outof = models.IntegerField()
        h_percentage = models.IntegerField()

        hostel_fees = models.IntegerField()
        recipt = models.IntegerField()







        
