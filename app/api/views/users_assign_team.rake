def assign_user_to_team(user, team)
  ActiveRecord::Base.transaction do
    user.teams << [team]
    user.save!
    puts "Assigned user #{user.uid} to #{team.name}"
  end
end

def prompt_for_user
  User.order(:id).all.each do |u|
    puts "[#{u.id}] #{u.uid}"
  end
  puts
  print "Which user do you want to assign a team to? "
  User.find(STDIN.gets.chomp)
rescue ActiveRecord::RecordNotFound => e
  puts "Couldn't find a user with id #{e.id}. Aborting."
  exit
end

def prompt_for_team
  Team.order(:id).all.each do |t|
    puts "[#{t.id}] #{t.name}"
  end
  puts
  print  "Which team id do you want to assign? "
  Team.find(STDIN.gets.chomp)
rescue ActiveRecord::RecordNotFound => e
  puts "Couldn't find a template with id #{e.id}. Aborting."
  exit
end

namespace :users do
  desc "Assign a team to a user"
  task assign_team: :environment do
    puts
    user = prompt_for_user
    puts
    team = prompt_for_team
    puts "Confirm that you want to assign #{user.uid} to #{team.name}."
    assign_user_to_team(user, team)
  end
end
