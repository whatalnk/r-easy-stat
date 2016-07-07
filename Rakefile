require 'fileutils'
desc "build .ipynb to .html in gh-pages dir"
task :build do
  target_dir = "gh-pages"
  Dir.glob("*.ipynb").each do |f|
    html = File.basename(f, ".ipynb") + ".html"
    if FileUtils.uptodate?("#{target_dir}/#{html}", [f]) then
      puts "#{html} is up to date"
    else
      puts "#{f} => #{target_dir}/#{html}"
      system("jupyter nbconvert --config jupyter_nbconvert_config.py #{f}")
      puts "\n"
    end
  end
end

desc "README.md => index.html"
task :toc do
  from = "README.md"
  to = "gh-pages/index.html"
  if FileUtils.uptodate?(to, [from]) then
    puts "#{to} is up to date"
  else
    puts "#{from} => #{to}"
    system("pandoc #{from} -o #{to}")
  end
end
