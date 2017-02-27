require 'rails_helper'

RSpec.describe TaxonomyImporter, type: :model do

  before(:each) do
    @importer = TaxonomyImporter.new
  end

  it "should import rows from the csvs" do
    @importer.import

    expect(MeasureAverage.count).not_to be(0)
    expect(Topic.count).not_to be(0)
    expect(Measure.count).not_to be(0)
  end


  it "should import all measures" do
    require 'csv'
    total_measures_in_csv =
      CSV.read(Rails.root.join("./data/output/taxonomy.csv"),  encoding: "ISO8859-1:utf-8")
        .select{|r| r[5] == "T4"}.count
    @importer.import_measures
    expect(total_measures_in_csv).to eql(Measure.count)
  end

  it "should import measures with the correct topic" do
    pending "to be implemented..."
  end

  it " should delete old data on import" do
    @importer.import
    counts = [ MeasureAverage.count, Topic.count, Measure.count]

    @importer.import
    new_counts = [ MeasureAverage.count, Topic.count, Measure.count]

    new_counts.each_with_index do |count, index|
      expect(counts[index]).to eql count
    end
  end

  it "should import topics" do
    require 'csv'
    total_topics_in_csv =
      CSV.read(Rails.root.join("./data/output/taxonomy.csv"),  encoding: "ISO8859-1:utf-8")
        .tap{ |t| t.shift }
        .reject{|r| r[5] == "T4"}.count
    @importer.import_topics
    binding.pry
    expect(total_topics_in_csv).to eql(Topic.count)
  end
end
