# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

# Gudlft V1.1.0 Updates & Tests

## Testing

All tests are made with PyTest.

Directory location : `/tests`

How to use PyTest ? In your terminal :

```
pytest
```

## Fix

- Gudlft v1.0.0:
    - refactorisation of previous project : [Python_Testing](https://github.com/OpenClassrooms-Student-Center/Python_Testing)

- Gudlft v1.0.1:
    - Fixing [ERROR: Entering a unknown email crashes the app](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/1)
    - Branch : BUG/ISSUE1_Error_entering_unknown_email
    - Folder '/features' : containing all test database

- Gudlft v1.0.2:
    - Fixing [BUG: Clubs should not be able to use more than their points allowed](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/2)
    - Branch: BUG/ISSUE2_points_allowed

- Gudlft v1.0.3:
    - Fixing [BUG: Clubs shouldn't be able to book more than 12 places per competition](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/4)
    - Branch: BUG/ISSUE4_no_more_than_12_places

- Gudlft v1.0.4:
    - Fixing [BUG: Booking places in past competitions](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/5)
    - Branch: BUG/ISSUE5_booking_past_competition

- Gudlft v1.0.5:
    - Fixing [BUG: Point updates are not reflected](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/6)
    - Branch: BUG/ISSUE6_point_updates_not_reflected

- Gudlft v1.1.0:
    - New feature: [FEATURE: Implement Points Display Board](https://github.com/OpenClassrooms-Student-Center/Python_Testing/issues/7)
    - Branch: FUNCTIONALITY/phase2_points_clubs
    - Added new template '/templates/board.html' to display club's points board. Clubs board can be access from the welcome page. Everyone can access to it.

## Performance tests

### Locust

In your terminal:
```
cd tests/performance_tests
locust
```

result with 6 users:
![le_cam_matthieu_2_2_statistics_apres](https://user-images.githubusercontent.com/85108007/165518282-aaea887a-5b79-4f2a-b547-c6192c590f79.PNG)
![le_cam_matthieu_2_4_number_of_users_apres](https://user-images.githubusercontent.com/85108007/165518299-e6f6afe3-fd59-411f-bb3a-cd52be67a3e1.png)
![le_cam_matthieu_2_6_response_times_(ms)_apres](https://user-images.githubusercontent.com/85108007/165518303-62a4441e-b987-43d5-907b-dc5bfaaf634e.png)
![le_cam_matthieu_2_8_total_requests_per_second_apres](https://user-images.githubusercontent.com/85108007/165518320-1b6ac0aa-2627-4fef-b46c-6557c87c8076.png)

### Coverage

In your terminal:
```
coverage run -m pytest
coverage html
```

result:

![le_cam_matthieu_2_2_coverage_apres](https://user-images.githubusercontent.com/85108007/165518546-144af968-c131-4890-95fe-ae2c90e79d7d.PNG)


