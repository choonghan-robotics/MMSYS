# Use the uploaded ACM bundle without modifying or duplicating its files.
# The trailing default path keeps the TeX installation's standard packages.
# BibTeX may run inside an output directory; retain the source-template path.
use Cwd qw(abs_path);
my $template_root = abs_path('./acmart-primary');
$ENV{'TEXINPUTS'} = $template_root . '//:' . ($ENV{'TEXINPUTS'} // '');
$ENV{'BSTINPUTS'} = $template_root . '//:' . ($ENV{'BSTINPUTS'} // '');
$pdf_mode = 1;
