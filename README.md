## Job Portal Project Practice

### Models:
- Custom User (Both)
    - username
    - password
    - confirm password (only in frontend)
    - role (recruiter, jobseeker)
    - city
    - gender
    - profile picture
    - email
    - User Type
        - Recruiters
        - JobSeekers

- Basic Information(Both)
    - portaluser (onetoonefield)
    - Father's name
    - mother's name
    - dob
    - marital status

- Contact details (Both)
    - portaluser (onetoonefield)
    - mobile
    - emergency contact
    - present address
    - permanent address

- Educatinal qualification (Job Seekers)
    - seekeruser (forigenkey)
    - Degree
    - Passing year
    - grade
    - department

- Work Experience (Job Seeker)
    - seekeruser (forigenkey)
    - Company Name
    - Designation
    - Duration

- Job Model (Recruiters)
    - recruiteruser (forigenkey)
    - Job title
    - company description
    - company logo
    - company name
    - company location
    - qualifications
    - deadline
    - salary

- Job Apply Model (Seeker)
    - Applicant (forigenkey)
    - Applied Job (forigenkey)
    - Resume 
    - Profile Pic
    - Skills
    - Status