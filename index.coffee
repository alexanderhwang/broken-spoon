$ ->
  $.get "/persons", (persons) ->
    $.each persons, (index, person) ->
      $("#persons").append $("<li>").text person.name
  $.get "/things", (things) ->
    $.each things, (index, thing) ->
      $("#things").append $("<li>").text thing.thingName
  $.get "/display", (display) ->
     $("#display").append display
