set -o errexit

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
  echo -e "Starting to update gh-pages\n"

  #go to home and setup git
  cd $HOME
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis"

  #using token clone gh-pages branch
  git clone --quiet --branch=gh-pages https://${GH_TOKEN}@github.com/tdhock/PeakError  gh-pages
  git clone --quiet --branch=master https://${GH_TOKEN}@github.com/tdhock/PeakError  master

  #go into master directory and run the Rperform functions
  cd master
  touch temp_Rperform.R
  echo "Rperform::plot_webpage(test_directory = \"./tests/\")" >> temp_Rperform.R
  Rscript temp_Rperform.R
  rm temp_Rperform.R

  cd ../gh-pages
  cp -Rf $HOME/master/index.html index.html

  #add, commit and push files
  git add -f .
  git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to gh-pages"
  git push -fq origin gh-pages

  echo -e "Done magic with Rperform\n"
fi
