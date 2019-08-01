/** @description Variavel que guarda informacoes sobre mim. */
var bio = {
	"name": "Gabriel Santiago",
	"age": 18,
	"role": "Web Developer",
	"contacts": {
		"email": "gabrielmssantiago@gmail.com",
		"mobile": "9 9999 9999",
		"location": "Uberlandia",
		"github": "https://github.com/gabrielmendes98"
	},
	"welcomeMessage": "The only way to great work is to love what you do.",
	"skills": ["Android Development", "Java", "Python", "JavaScript", "HTML", "CSS", "Bootstrap", "JQuery", "C/C++" ],
	"biopic": "images/me.jpg" 
};

/** @description Variavel que guarda informacoes sobre os trabalhos que ja fiz. */
var work = {
	'jobs': [
		{
			"employer": "Universidade Federal de Uberlandia",
			"title": "Student",
			"datesWorked": "2017 - Present", 
			"location": "Universidade Federal de Uberlandia, Uberlandia, Minas Gerais, Brasil",
			"description": "I am pursuing my Bachelor degree here."
		},
		{
			"employer": "Universidade de Sao Paulo",
			"title": "Teacher",
			"datesWorked": "2010 - 2016",
			"location": "Universidade de Sao Paulo, Sao Paulo, Sao Paulo, Brasil",
			"description": "I taught everyday"
		}
	]
};

/** @description Variavel que guarda informacoes sobre a educacao que tive. */
var education = {
	"schools": [
		{
			"name": "Universidade Federal de Uberlandia",
			"location": "Uberlandia",
			"degree": "Studying",
			"major": ["Computer Science"],
			"dates": "2016 - Present",
			"url": "http://www.ufu.br"
		}
	],
	"onlineCourses": [
		{
			"title": "Intro programming",
			"school": "Udacity",
			"dates": "2017 - Present",
			"url": "https://classroom.udacity.com/nanodegrees/nd000"
		}
	]
};

/** @description Variavel que guarda informacoes sobre os projetos que ja fiz. */
var projects = {
	"projects": [
		{
			"title": "Website",
			"dates": "January 2017 - February 2017",
			"description": "A movie trailer website",
			"images": ["images/website.png"]
		}
	]
};

/** @description Adiciona a variavel bio a pagina. */
bio.display = function(){
	var i;
	var formattedName = HTMLheaderName.replace("%data%", bio.name);
	var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
	var formattedPicture = HTMLbioPic.replace("%data%", bio.biopic);
	var formattedWelcomeMsg = HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage);

	var formattedContactInfo = [];
	formattedContactInfo.push(HTMLemail.replace("%data%", bio.contacts.email));
	formattedContactInfo.push(HTMLgithub.replace("%data%", bio.contacts.github));
	formattedContactInfo.push(HTMLmobile.replace("%data%", bio.contacts.mobile));
	formattedContactInfo.push(HTMLlocation.replace("%data%", bio.contacts.location));

	$("#header").prepend(formattedRole);
	$("#header").prepend(formattedName);
	$("#header").append(formattedPicture);
	$("#header").append(formattedWelcomeMsg);

	if(bio.skills.length > 0) {
		$("#header").append(HTMLskillsStart);

		for(i in bio.skills) {
			$("#skills").append(HTMLskills.replace("%data%", bio.skills[i]));
		}
	}

	for(i in formattedContactInfo) {
		$("#topContacts").append(formattedContactInfo[i]);
		$("#footerContacts").append(formattedContactInfo[i]);
	}
}

bio.display();

/** @description Adiciona a variavel work a pagina. */
work.display = function(){
	var i;
	if(work.jobs.length > 0) {
	
		$("#workExperience").append(HTMLworkStart);

		for(i in work.jobs) {
			var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[i].employer);
			var formattedWorkTitle = HTMLworkTitle.replace("%data%", work.jobs[i].title);
			var formattedWorkLocation = HTMLworkLocation.replace("%data%", work.jobs[i].location);
			var formattedDatesWorked = HTMLworkDates.replace("%data%", work.jobs[i].datesWorked);
			var formattedWorkDescription = HTMLworkDescription.replace("%data%", work.jobs[i].description);

			var formattedEmployerWorkTitle = formattedEmployer + formattedWorkTitle;

			$(".work-entry:last").append(formattedEmployerWorkTitle);
			$(".work-entry:last").append(formattedWorkLocation);
			$(".work-entry:last").append(formattedDatesWorked);
			$(".work-entry:last").append(formattedWorkDescription);
		}

	}
}

work.display();

/** @description Adiciona a variavel projects a pagina. */
projects.display = function() {
	var i;
	if(projects.projects.length > 0) {
		for(i in projects.projects) {
			$("#projects").append(HTMLprojectStart);

			var formattedProjectTitle = HTMLprojectTitle.replace("%data%", projects.projects[i].title).replace("#", projects.projects[i].url);
			var formattedProjectDates = HTMLprojectDates.replace("%data%", projects.projects[i].dates);
			var formattedProjectDescription = HTMLprojectDescription.replace("%data%", projects.projects[i].description);

			$(".project-entry:last").append(formattedProjectTitle);
			$(".project-entry:last").append(formattedProjectDates);
			$(".project-entry:last").append(formattedProjectDescription);

			for(img in projects.projects[i].images) {
				var formattedProjectImage = HTMLprojectImage.replace("%data%", projects.projects[i].images[img]);
				$(".project-entry:last").append(formattedProjectImage);
			}
			

		}
	}
}

projects.display();

/** @description Adiciona a variavel education a pagina. */
education.display = function() {
	var i;
	if(education.schools.length > 0 || education.onlineCourses.length > 0) {
		for(i in education.schools) {
			$("#education").append(HTMLschoolStart);

			var formattedSchoolName = HTMLschoolName.replace("%data%", education.schools[i].name).replace("#", education.schools[i].url);
			var formattedSchoolDegree = HTMLschoolDegree.replace("%data%", education.schools[i].degree);
			var formattedSchoolDates = HTMLschoolDates.replace("%data%", education.schools[i].dates);
			var formattedSchoolLocation = HTMLschoolLocation.replace("%data%", education.schools[i].location);

			$(".education-entry:last").append(formattedSchoolName + formattedSchoolDegree);
			$(".education-entry:last").append(formattedSchoolDates);
			$(".education-entry:last").append(formattedSchoolLocation);
			$(".education-entry:last").append(formattedSchoolMajor);

			for(m in education.schools[i].major){
				var formattedSchoolMajor = HTMLschoolMajor.replace("%data%", education.schools[i].major[m]);
				$(".education-entry:last").append(formattedSchoolMajor);
			}
		}

		if(education.onlineCourses.length > 0) {
			$("#education").append(HTMLonlineClasses);
			for(i in education.onlineCourses) {
				$("#education").append(HTMLschoolStart);
				var formattedOnlineTitle = HTMLonlineTitle.replace("%data%", education.onlineCourses[i].title).replace("#", education.onlineCourses[i].url);
				var formattedOnlineSchool = HTMLonlineSchool.replace("%data%", education.onlineCourses[i].school);
				var formattedOnlineDates = HTMLonlineDates.replace("%data%", education.onlineCourses[i].dates);
				var formattedOnlineURL = HTMLonlineURL.replace("%data%", education.onlineCourses[i].url).replace("#", education.onlineCourses[i].url);

				$(".education-entry:last").append(formattedOnlineTitle + formattedOnlineSchool);
				$(".education-entry:last").append(formattedOnlineDates);
				$(".education-entry:last").append(formattedOnlineURL);
			}
		}
		
	}
}

education.display();

/** @description Mostra no console a localizacao em (x,y) de onde o usuario clicou. */
$(document).click(function(loc) {
	var x = loc.pageX;
	var y = loc.pageY;

	logClicks(x,y);
});

/** @description Adiciona um botao ao final da pagina */
$("#main").append(internationalizeButton);

/** @description Adiciona o mapa do google com a localizacao de onde ja trabalhei ao subtopico da pagina chamado "Where I've Lived and Worked" */
$("#mapDiv").append(googleMap);