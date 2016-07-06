desc "build .ipynb to .html in gh-pages dir"
task :build do
    Dir.glob("*.ipynb").each do |f|
        system("jupyter nbconvert --config jupyter_nbconvert_config.py #{f}")
    end
end
