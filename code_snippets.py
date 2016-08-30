def intro(name='Hayden Blauzvern',
          college='Harvey Mudd College',
          class_of=2016,
          graduated=True):
    """Facts about me"""
    majors = ['Computer Science', 'Linguistics']
    interests = ['Programming', 'Security', 'Legos', 'Music', 'Photography']
    return (name, college, class_of, graduated, majors, interests)

def skills():
    """Skills I've acquired"""
    languages = ['Python', 'Java', 'C++', 'C', 'Scala']
    titles = ['Software Engineer', 'Security Engineer', 'Penetration Tester']
    return (languages, titles)

def projects(github='haydentherapper'):
    """Projects from college and in my free time"""
    my_projects = {}
    my_projects['Progettare'] = 'Designing and visualizing block constructions'
    my_projects['White Hat'] = 'Educational computer security iPad game'
    my_projects[
        'Cryptopals Solutions'] = 'Cryptographic challenge solutions in Python'
    return (github, my_projects)

def work_experience():
    """My work"""
    jobs = {}
    jobs['Microsoft'] = ('Software Engineer for Yammer', 'Current')
    jobs['Praetorian'] = ('Security Engineer', 'Summer 2014 and Summer 2015')
    jobs['Harvey Mudd'] = ('Undergraduate Researcher', 'Summer 2013')
    what_I_did = {}
    what_I_did['Praetorian'] = [
        'Penetration testing for web, mobile and desktop applications',
        ('Researched Man-in-the-Middle TLS protocol downgrade attack',
         'https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack'),
        'Vulnerability research using reverse engineering and fuzzing',
        ('Designed a game based on Mastermind used in hiring process',
         'https://www.praetorian.com/challenges/mastermind/'),
        ('Developed cryptography/steganography challenges used in hiring process',
         'https://www.praetorian.com/challenges/crypto/')
    ]
    what_I_did['Harvey Mudd'] = [
        ('Further developed "Impro-Visor"',
         'https://www.cs.hmc.edu/~keller/jazz/improvisor/'),
        'Created a style recognition tool to critique melodies and predict style'
    ]
    return (jobs, what_I_did)
