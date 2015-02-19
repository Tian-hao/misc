#! /usr/bin/perl -w
use strict;

my $countline = 0;
my $in;
while($in = <>)
{
	chomp $in;
	if ($in =~ />/ and $countline == 0)
	{print $in, "\n"; $countline ++;}
	elsif ($in =~ />/ and $countline > 0){print "\n", $in, "\n";}
	else 
	{print $in;}
	}
