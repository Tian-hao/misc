#! /usr/bin/perl -w
use strict;

my $in;
while($in = <>)
{
	chomp $in;
	my $leng = length $in;
	my $x = 0;
	while($x < $leng)
		{
			my $k = substr ($in, $x, 60);
			print $k, "\n";
			$x = $x + 60;
			}
		}
