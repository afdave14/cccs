use FileHandle;
	use LWP::UserAgent;
	$ua = LWP::UserAgent->new;
	$baseurl = "http://www.retrosheet.org/";
	for ($year = 60; $year <= 99; $year++) {
	  foreach $league ("al", "nl") {   
	   my $filename = '19' . $year . $league . '.zip';
	   my $url = $baseurl . '19' . $year . '/19' . $year . $league . '.zip';
	   my $req = HTTP::Request->new(GET => $url);
	   my $res = $ua->request($req);
	   print STDERR "fetching $filename\n";

	   if ($res->is_success) {
	      my $fh = new FileHandle ">$filename";
	      if (defined $fh) {     
	         print $fh $res->content;
	         $fh->close;
	      } else {
	         print STDERR "could not open file $filename: $!\n";
	      }
	   }
	   else {
	      print STDERR $res->status_line, "\n";
	   }
	  }
	}
	$league = 'ml';
	for ($year = 00; $year <= 09; $year++) {
	   my $filename = '200' . $year . $league . '.zip';  
	   my $url = $baseurl . '200' . $year . '/200' . $year . $league . '.zip';
	   my $req = HTTP::Request->new(GET => $url);
	   my $res = $ua->request($req);

	   print STDERR "fetching $filename\n";

	   if ($res->is_success) {
	      my $fh = new FileHandle ">$filename";
	       if (defined $fh) {     
	          print $fh $res->content;
	          $fh->close;
	       } else {
	         print STDERR "could not open file $filename: $!\n";
	       }
	   }
	   else {
	      print STDERR $res->status_line, "\n";
	   }
	}