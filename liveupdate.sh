# Watch a postscript file for changes to live-update an image.

ps_file=$1
base_name="${ps_file%.*}"

while true; do
  inotifywait -e modify,close_write,move_self,create,delete_self "examples/$ps_file"
  gs -dNOSAFER -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile="images/${base_name}.pdf" "examples/$ps_file"
  convert -density 300 "images/${base_name}.pdf" -background white -flatten -resize 200% "images/${base_name}.png"
  rm -f "images/${base_name}.pdf"
  sleep 0.1
done