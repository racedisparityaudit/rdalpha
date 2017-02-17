require 'rails_helper'

RSpec.describe TaxonomyImporter, type: :model do

  it "should import measure averages" do

    #TODO: finish writing this rspec wasn't working KASM
    path = Rails.root.join("/spec/fixtures/measure_averages.csv").to_s

    TaxonomyImporter.import(path)

    expect(MeasureAverage.count).not_to be(0)
  end

end
