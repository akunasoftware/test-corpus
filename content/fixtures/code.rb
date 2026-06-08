Task = Data.define(:queue, :priority, :detail)

def format_tasks(tasks)
  tasks.map do |task|
    "#{task.queue} priority #{task.priority}: #{task.detail}"
  end
end

tasks = [
  Task.new("imports", 2, "source file received"),
  Task.new("reviews", 1, "extraction fixture marker: shared code sample"),
  Task.new("exports", 3, "summary report queued")
]

puts(format_tasks(tasks))
