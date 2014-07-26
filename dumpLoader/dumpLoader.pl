#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use YAML::Syck qw(LoadFile);

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
$fileContent =~ s/^/var: /;
open(OUTY, '>', 'file.yaml');
print OUTY $fileContent;
close(OUTY);
open(OUT, '>', 'file.out');
my $hash = LoadFile("file.yaml");
my $mas_array = $hash->{var};
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
system 'rm file.yaml';
