#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

open(my $F, '<', 'file.in');
my $fileContent;
binmode($F);
{
 local $/;
 $fileContent = <$F>;
}
close($F);

$fileContent =~ s/\(/\[/g;
$fileContent =~ s/\)/\]/g;
$fileContent =~ s/^/\$mas_array=/;
my $mas_array;
eval($fileContent);

open(OUT, '>', 'file.out');
pars_array($mas_array);
print OUT "CONS\n";

sub pars_array {
    my $mas = shift;
    for(@$mas) {
       if(ref $_ eq 'ARRAY') {
            pars_array($_);
            print OUT "CONS\n";
            next;
       } 
       print OUT "LDC $_\n";
    }
    return;
}
close(OUT);
